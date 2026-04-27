import { useEffect, useState } from "react"
import { useApp } from "../context/AppContext"
import { getRoute } from "../services/api"
import MapView from "../components/MapView"
import { useNavigate } from "react-router-dom"






const NavigatePage = () => {
  const { selectedStore, scanPointId } = useApp()
  const [routePath, setRoutePath] = useState(null)
  const navigate = useNavigate()

  useEffect(() => {
    if (!selectedStore || !scanPointId) return
    const fetchRoute = async () => {
      const data = await getRoute(scanPointId, selectedStore.id)
      setRoutePath(data.route)
    }
    fetchRoute()
  }, [])

  if (!selectedStore || !scanPointId) {
    return <p>No store or scan point selected. Go back to chat.</p>
  }

  return (
    <div>
      <h3>Navigation to {selectedStore.name}</h3>
      <MapView routePath={routePath} />
      {selectedStore.id && <button onClick={() => navigate("/coupon")}>Coupons</button>}
      <button onClick={() => navigate("/")}>Back to chat</button>
    </div>
  )
}

export default NavigatePage