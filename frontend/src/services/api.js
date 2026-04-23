
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
    const response = await fetch(`${BASE_URL}/session/scan`, {
        method: "POST",
        headers:  { "Content-Type": "application/json" },
        body: JSON.stringify({ scan_point_id: scanPointId })
    })
    const data = await response.json()
    return data
}

const createSession = async () => {
    const response = await fetch(`${BASE_URL}/session/create`, {
        credentials: "include"
    })
    const data = await response.json()
    return data
}

const claimCoupon = async (couponCode) => {
    const response = await fetch(`${BASE_URL}/coupon/claim`,{
        method: "POST",
        headers:  { "Content-Type": "application/json" }, 
        body: JSON.stringify({coupon_code: couponCode})
    })

    const data = await response.json()
    return data
}

const getRoute  = async (scanPointId,storeId) => {
    const response = await fetch(`${BASE_URL}/navigate/${scanPointId}/${storeId}`)
    const data = await response.json()
    return data
}

const getCurrentAd = async () => {
    const response = await fetch(`${BASE_URL}/screen/current-ad`)
    const data = await response.json()
    return data
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