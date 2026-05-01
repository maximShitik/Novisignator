import { useState } from "react"


const Composer = ({onSend}) => {
    const [input , setInput] = useState("")

        const handleClick = async () => {
        if (!input) return
        onSend(input)
        setInput("")
    }

return (
    <div className="p-3 border-t flex gap-2 shrink-0 border-2 ">
        <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Write a massage"
            className="flex-1 px-4 py-2 border rounded-xl outline-none focus:border-blue-500"
        />
        <button onClick={handleClick} className=" px-5 py-2 bg-blue-600 text-white rounded-xl font-semibold hover:bg-blue-700 whitespace-nowrap">
            send
        </button>
    </div>
)
}
export default Composer
