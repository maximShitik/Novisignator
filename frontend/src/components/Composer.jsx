import { useState } from "react"


const Composer = ({onSend}) => {
    const [input , setInput] = useState("")

        const handleClick = async () => {
        if (!input) return
        onSend(input)
        setInput("")
    }

return (
    <div className="p-3 border-t flex gap-2 shrink-0 ">
        <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Write a message"
            className="flex-1 px-4 py-2 bg-gray-100 rounded-full outline-none focus:ring-2 focus:ring-blue-500"
        />
        <button onClick={handleClick} className=" w-10 h-10 rounded-full bg-blue-600 flex items-center justify-center text-white hover:bg-blue-700 active:bg-blue-800">
            ⫸
        </button>
    </div>
)
}
export default Composer
