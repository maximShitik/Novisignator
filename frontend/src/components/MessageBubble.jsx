import "./MessageBubble.css"

const MessageBubble = ({text,sender}) =>{
    return <p className={`message message--${sender}`} dir="auto">{text}</p>
}

export default MessageBubble