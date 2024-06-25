"use client";

import { QuestionMessage } from "@/components/Messages";

import { useActions, useUIState } from "ai/rsc";
import { FormEvent } from "react";
import { AI, ClientMessage } from "@/app/action";

export default function Home() {
  const { sendMessage } = useActions<typeof AI>();
  const [messages, setMessages] = useUIState();

  const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    const target = event.target as typeof event.target & {
      message: { value: string };
    };
    const message = target.message.value;

    const newMessages = [
      ...messages,
      {
        id: Date.now(),
        role: "user",
        display: <QuestionMessage content={message} />,
      },
    ];
    setMessages(newMessages);

    const response = await sendMessage(message);

    setMessages([...newMessages, ...response]);
  };

  return (
    <div className="h-screen flex flex-col w-full max-w-md py-24 mx-auto stretch ">
      <div className="flex-1">
        <ul>
          {messages.map((message: ClientMessage) => (
            <div key={message.id}>{message.display}</div>
          ))}
        </ul>
      </div>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="message"
          className="fixed bottom-0 p-3 border-2 rounded-lg mb-8 w-full max-w-md"
          placeholder="テキストを入力してください"
        />
      </form>
    </div>
  );
}
