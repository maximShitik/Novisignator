import { useState } from "react";
import { sendMessage } from "../services/api";
import { useApp } from "../context/AppContext";
import MessageBubble from "../components/MessageBubble";
import Composer from "../components/Composer";
import ConfirmPrompt from "../components/ConfirmPrompt";

const ChatPage = () => {
  const [messages, setMessages] = useState([]);
  const { setSelectedStore } = useApp();

  const handleSend = async (userMessage) => {
    setMessages([...messages, { text: userMessage, sender: "user" }]);

    const response = await sendMessage(userMessage);
    setMessages((prev) => [
      ...prev,
      { text: response.response, sender: "bot" },
    ]);

    if (response.store_id) {
      setSelectedStore({ id: response.store_id, name: response.store_name });
      setMessages(prev => [...prev, {text:"Want a coupon?", sender:"bot", type:"prompt"}])
    }
  };

  return (
    <div>
      <h1>Chat</h1>
      <div>
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
