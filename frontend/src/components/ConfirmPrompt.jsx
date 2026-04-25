

const ConfirmPrompt = ({ text, onYes, onNo })=> {

    return(
        <div>
            <p> {text}</p>
            <button onClick={onYes}>Yes</button>
            <button onClick={onNo}>No, navigate</button>
        </div>
    )

}

export default ConfirmPrompt