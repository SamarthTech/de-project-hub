//import React from "react";
import "./Weather.css";
import search_icon from "../assets/search.png";
import clear_icon from "../assets/clear.png";
import cloud_icon from "../assets/cloud.png";
import humidity_icon from "../assets/humid.jpg";
import drizzle_icon from "../assets/drizzle.jpg";
import rain_icon from "../assets/rain.png";
import snow_icon from "../assets/snow.png";
import wind_icon from "../assets/wind.jpg";
import { useEffect } from "react";
import { useState } from "react";
import { useRef } from "react";

const Weather = () => {
  const inputRef = useRef();
  const [weatherData, setWeatherData] = useState(false);

  const allIcons = {
    "01d": clear_icon,
    "01n": clear_icon,
    "02d": cloud_icon,
    "02n": cloud_icon,
    "03d": cloud_icon,
    "03n": cloud_icon,
    "04d": drizzle_icon,
    "04n": drizzle_icon,
    "09d": rain_icon,
    "09n": rain_icon,
    "10d": rain_icon,
    "10n": rain_icon,
    "13d": snow_icon,
    "13n": snow_icon,
  };

  const search = async (city) => {
    if (city === "") {
      alert("Enter city name!!");
      return;
    }

    try {
      const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&units=metric&appid=${
        import.meta.env.VITE_APP_ID
      }`;

      const response = await fetch(url);
      const data = await response.json();

      /*if (response.ok) {
        alert(data.message);
        return;
      }*/
      console.log(data);

      const icon = allIcons[data.weather[0].icon] || clear_icon;
      setWeatherData({
        humidity: data.main.humidity,
        windSpeed: data.wind.speed,
        temperature: Math.floor(data.main.temp),
        pressure:data.main.pressure,
        feels_like: data.main.feels_like,
        location: data.name,
        icon: icon,
        
      });
    } catch (error) {
      setWeatherData(false);
      console.error("Error in fetching weather data", error);
    }
  };
  useEffect(() => {
    search("Kolkata");
  }, []);
  return (
    <div className="weather">
      <div className="search-bar">
        <input ref={inputRef} type="text" placeholder="Search" />
        <img
          src={search_icon}
          alt=""
          onClick={() => search(inputRef.current.value)}
        />
      </div>
      {weatherData ? (
        <>
          <img src={weatherData.icon} alt="" className="weather-icon" />
          <p className="temp">{weatherData.temperature}°C</p>
          
          
          <p>Feels like {weatherData.feels_like}°C</p>
          <p className="location">{weatherData.location}</p>
          <div className="weather-data">
            <div className="col">
              <img
                src={humidity_icon}
                alt=""
                style={{ width: "50px", height: "50px" }}
              />
              <div>
                <p>{weatherData.humidity}%</p>
                <span>Humidity</span>
              </div>
              <div>
                <p>{weatherData.pressure}hPa</p>
                <span>Pressure</span>
              </div>
            </div>
            <div className="col">
              <img
                src={wind_icon}
                alt=""
                style={{ width: "50px", height: "50px" }}
              />
              <div>
                <p>{weatherData.windSpeed}Km/hr</p>
                <span>Wind</span>
              </div>
            </div>
          </div>
        </>
      ) : (
        <></>
      )}
    </div>
  );
};

export default Weather;
