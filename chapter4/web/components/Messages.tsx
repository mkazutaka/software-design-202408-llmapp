type QuestionMessageProps = {
  content: string;
};
export const QuestionMessage = (props: QuestionMessageProps) => (
  <div className="py-2">
    <p className="text-3xl">{props.content}</p>
  </div>
);

type SearchMessageProps = {
  content: string;
};
export const SearchMessage = (props: SearchMessageProps) => (
  <div className="py-2">
    <p className="text-gray-500">「{props.content}」 で検索</p>
  </div>
);

type SourceMessageProps = {
  sources: string[];
};
export const SourceMessage = (props: SourceMessageProps) => (
  <div className="py-2">
    <h2 className="text-lg font-bold pb-1">Sources</h2>
    <ol className="list-decimal text-sm pl-4">
      {props.sources.map((source, index) => (
        <li key={index}>{source}</li>
      ))}
    </ol>
  </div>
);

type AnswerMessageProps = {
  content: string;
};
export const AnswerMessage = (props: AnswerMessageProps) => (
  <div className="py-2">
    <h2 className="text-lg font-bold pb-1">Answer</h2>
    <div className="text-base">{props.content}</div>
  </div>
);
