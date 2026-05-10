import { useState } from "react";
import { sendMessage } from "../services/api";
import { useApp } from "../context/AppContext";
import MessageBubble from "../components/MessageBubble";
import Composer from "../components/Composer";
import ConfirmPrompt from "../components/ConfirmPrompt";
import { useNavigate } from "react-router-dom";

const ChatPage = () => {
  const [messages, setMessages] = useState([]);
  const { setSelectedStore } = useApp();
  const navigate = useNavigate();

  const handleSend = async (userMessage) => {
    setMessages([...messages, { text: userMessage, sender: "user" }]);

    const response = await sendMessage(userMessage);
    setMessages((prev) => [
      ...prev,
      { text: response.response, sender: "bot" },
    ]);

    if (response.store_id) {
      console.log("SETTING STORE:", response.store_id, response.store_name);
      setSelectedStore({ id: response.store_id, name: response.store_name });
      setMessages((prev) => [
        ...prev,
        { text: "Want a coupon?", sender: "bot", type: "prompt" },
      ]);
    }
  };

  return (
    <div
      className="max-w-lg w-full h-full flex flex-col  bg-white shadow-lg rounded-xl overflow-hidden "
      
    >
      <div className="p-4 border-b flex justify-between items-center">
        <div className="flex items-center gap-2">
          <div className="w-9 h-9 rounded-full bg-blue-600 flex items-center justify-center text-white">
            N
          </div>
          <div>
            <h1 className="text-lg font-semibold">MallAssistant</h1>
            <p className="text-xs text-gray-500">
              Smart shopping assistant
            </p>
          </div>
        </div>
        <p className="bg-green-100 text-green-700 px-2 py-1 rounded-full">Active</p>
      </div>
      <div className="flex-1 overflow-y-auto py-4 px-4 flex flex-col gap-2">
        {messages.map((msg, index) => {
          if (msg.type === "prompt") {
            return (
              <ConfirmPrompt
                key={index}
                text={msg.text}
                onYes={() => navigate("/coupon")}
                onNo={() => navigate("/navigate")}
              />
            );
          }
          return (
            <MessageBubble key={index} text={msg.text} sender={msg.sender} />
          );
        })}
      </div>
      <Composer onSend={handleSend} />
    </div>
  );
};

export default ChatPage;
