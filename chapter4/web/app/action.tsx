import { createAI } from "ai/rsc";
import { createStreamableUI } from "ai/rsc";
import {
  AnswerMessage,
  SearchMessage,
  SourceMessage,
} from "@/components/Messages";
import { nanoid } from "nanoid";
import { ReactNode } from "react";

async function* createLangChainIterator(
  reader: ReadableStreamDefaultReader<Uint8Array>,
) {
  const decoder = new TextDecoder();
  let decodedData = "";

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;

    if (value) {
      decodedData += decoder.decode(value);
      let lines = decodedData.split("\r\n\r\n");
      decodedData = lines.pop() ?? ""; // 保留して次回のデータで処理する

      for (let line of lines) {
        line = line.replace("event: data", "");
        line = line.replace("event: end", "");
        line = line.replace("data:", "");
        line = line.trim();
        if (line === "") continue;
        yield JSON.parse(line);
      }
    }
  }
}

function createLangChainReader(
  reader: ReadableStreamDefaultReader<Uint8Array>,
) {
  const iterator = createLangChainIterator(reader);
  return new ReadableStream({
    async pull(controller) {
      const { value, done } = await iterator.next();
      if (done) {
        controller.close();
      } else {
        controller.enqueue(value);
      }
    },
  });
}

export async function sendMessage(message: string): Promise<ClientMessage[]> {
  "use server";

  const toolStreamUI = createStreamableUI();
  const messageStreamUI = createStreamableUI();
  const sleep = (ms: number) => new Promise((res) => setTimeout(res, ms));

  (async () => {
    const input = { input: { messages: [["user", message]] } };
    const response = await fetch("http://127.0.0.1:8000/graph/stream_events", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(input),
    });

    let content = "";
    const stremReader = createLangChainReader(response.body!.getReader());
    const reader = stremReader.getReader();
    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      if (!value) continue;

      const event = value["event"];
      if (event === "on_chat_model_stream") {
        if (value["data"]["chunk"].content) {
          content += value["data"]["chunk"].content;
          messageStreamUI.update(<AnswerMessage content={content} />);
        }
      } else if (event === "on_tool_start") {
        const query = value["data"]["input"]["query"];
        toolStreamUI.append(<SearchMessage content={query} />);
        await sleep(500);
      } else if (event === "on_tool_end") {
        const sources = value["data"]["output"].map(
          (output: any) => output.url,
        );
        toolStreamUI.append(<SourceMessage sources={sources} />);
        await sleep(500);
      }
    }
    toolStreamUI.done();
    messageStreamUI.done();
  })();

  return [
    {
      id: nanoid(),
      role: "assistant",
      display: toolStreamUI.value,
    },
    {
      id: nanoid(),
      role: "assistant",
      display: messageStreamUI.value,
    },
  ];
}

export type ServerMessage = {
  role: "user" | "assistant";
  content: string;
};

export type ClientMessage = {
  id: string;
  role: "user" | "assistant";
  display: ReactNode;
};

export const AI = createAI({
  actions: {
    sendMessage,
  },
  initialAIState: [] as ServerMessage[],
  initialUIState: [] as ClientMessage[],
});
