import { useState } from "react"


const Composer = ({onSend}) => {
    const [input , setInput] = useState("")

        const handleClick = async () => {
        if (!input) return
        onSend(input)
        setInput("")
    }

    return(
        <div>
             <input 
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Type a message..."
            />
            <button onClick ={handleClick}>
                Send
            </button>
        </div>
    )
}
export default Composer