

const MapView = ({routePath }) =>{
    return(
        <svg viewBox="0 0 500 500" width="500" height="500">
            <path d={routePath} stroke="blue" fill="none" strokeWidth="3" />
        </svg>
    )
}

export default MapView