import { BrowserRouter, Routes, Route } from "react-router-dom"
import { AppProvider } from "./context/AppContext"
import ChatPage from "./pages/ChatPage"
import CouponPage from "./pages/CouponPage"
import NavigatePage from "./pages/NavigatePage"
import ScreenPage from "./pages/ScreenPage"

const App = () => {
    return (
        <AppProvider>
            <BrowserRouter>
                <Routes>
                    <Route path="/" element={<ChatPage />} />
                    <Route path="/coupon" element={<CouponPage />} />
                    <Route path="/navigate" element={<NavigatePage />} />
                    <Route path="/screen" element={<ScreenPage />} />
                </Routes>
            </BrowserRouter>
        </AppProvider>
    )
}

export default App