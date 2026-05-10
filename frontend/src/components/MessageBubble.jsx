
const bubbleStyles = {
    user: "max-w-[80%] px-4 py-3 bg-blue-600 text-white self-end rounded-2xl rounded-tr-sm"
,
    bot: "max-w-[80%] px-4 py-3 bg-gray-100 text-gray-800 self-start rounded-2xl rounded-tl-sm"
}

const MessageBubble = ({text,sender}) =>{
    return <p className={bubbleStyles[sender]} dir="auto">{text}</p>
}

export default MessageBubble