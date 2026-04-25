import { useEffect, useState } from "react";
import { getCurrentAd } from "../services/api";

const ScreenPage = () => {
  const [adUrl, setAdUrl] = useState(null);

useEffect(() => {
    const getAd = async () => {
        const data = await getCurrentAd()
        setAdUrl(data.ad_url)
    }

    getAd()
    const timer = setInterval(getAd, 3000) 

    return () => clearInterval(timer)
}, [])

  return <div>{adUrl ? <img src={adUrl} /> : <p>No ad available</p>}</div>;
};

export default ScreenPage;
