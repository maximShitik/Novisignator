
const BASE_URL = "http://localhost:5000"

const request = async (endpoint, options = {}) => {
    const response = await fetch(`${BASE_URL}${endpoint}`, {
        ...options,
        credentials: "include"
    })
    const data = await response.json()
    return data
}

const sendMessage = async (message) => {
    return request("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message })
    })
}

const displayCoupons = async (storeId) => {

    return request(`/coupon/${storeId}`)
}

const registerScan = async (scanPointId) => {
    return request("/session/scan", {
        method: "POST",
        headers:  { "Content-Type": "application/json" },
        body: JSON.stringify({ scan_point_id: scanPointId })
        
    })
}

const createSession = async () => {

    return request("/session/create")
}

const claimCoupon = async (couponCode) => {

    return request("/coupon/claim",{
        method: "POST",
        headers:  { "Content-Type": "application/json" }, 
        body: JSON.stringify({coupon_code: couponCode})
    })
}

const getRoute  = async (scanPointId,storeId) => {
    return request(`/navigate/${scanPointId}/${storeId}`)
}

const getCurrentAd = async () => {

    return request("/screen/current-ad")
}


export {
    sendMessage,
    displayCoupons,
    claimCoupon,
    getRoute,
    getCurrentAd,
    createSession,
    registerScan
}