

const ConfirmPrompt = ({ text, onYes, onNo })=> {

    return(
        <div className="max-w-[85%]  px-4 py-3 bg-gray-100 text-gray-800 self-start rounded-2xl rounded-tl-sm">
            <p> {text}</p>
            <div className="flex gap-2 mt-3">
            <button onClick={onYes} className="flex-1 h-12 px-6 rounded-xl bg-blue-600 flex items-center justify-center text-white hover:bg-blue-700 active:bg-blue-800 ">Yes</button>
            <button onClick={onNo} className="flex-1 h-12 px-6 rounded-xl flex items-center justify-center bg-white text-gray-800 border border-gray-300 hover:bg-gray-400 active:bg-gray-400">No, Navigate</button>
            </div>
        </div>
    )

}

export default ConfirmPrompt