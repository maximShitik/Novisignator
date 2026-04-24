import { createContext, useState, useContext } from "react"

const AppContext = createContext()

const AppProvider = ({ children }) => {
    const [selectedStore, setSelectedStore] = useState(null)
    const [couponCode, setCouponCode] = useState(null)
    const [scanPointId, setScanPointId] = useState(null)

    return (
        <AppContext.Provider value={{
            selectedStore, setSelectedStore,
            couponCode, setCouponCode,
            scanPointId, setScanPointId
        }}>
            {children}
        </AppContext.Provider>
    )
}

const useApp = () => useContext(AppContext)

export { AppProvider, useApp }
