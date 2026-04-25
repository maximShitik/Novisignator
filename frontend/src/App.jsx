import { BrowserRouter, Routes, Route } from "react-router-dom";
import { AppProvider, useApp } from "./context/AppContext";
import ChatPage from "./pages/ChatPage";
import CouponPage from "./pages/CouponPage";
import NavigatePage from "./pages/NavigatePage";
import ScreenPage from "./pages/ScreenPage";
import { useEffect } from "react";
import { createSession, registerScan } from "./services/api";
import { useSearchParams } from "react-router-dom";

const AppInit = () => {
    const [searchParams] = useSearchParams()
    const { setScanPointId } = useApp()
    const scanPoint = searchParams.get("scan_point")

    useEffect(() => {
        const init = async () => {
            await createSession()

            if (scanPoint) {
                setScanPointId(scanPoint)
                await registerScan(scanPoint)
            }
        }
        init()
    }, [])

    return null
}

const App = () => {

  return (
    <AppProvider>
      <BrowserRouter>
        <AppInit />
        <Routes>
          <Route path="/" element={<ChatPage />} />
          <Route path="/coupon" element={<CouponPage />} />
          <Route path="/navigate" element={<NavigatePage />} />
          <Route path="/screen" element={<ScreenPage />} />
        </Routes>
      </BrowserRouter>
    </AppProvider>
  );
};

export default App;
