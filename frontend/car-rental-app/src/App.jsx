import React from 'react';


import "./App.css";
import AppRouting from "./AppRouting";
import Footer from "./components/Footer";
import Navbar from "./components/Navbar";

// Function to fetch car rental data
async function fetchCarRentalData() {
  const apiEndpoint = 'https:www.trawex.com/car-api.php';

  try {
      const response = await fetch(apiEndpoint);
      
      if (!response.ok) {
          throw new Error('Failed to fetch data');
      }

      const data = await response.json();
      return data;
  } catch (error) {
      console.error('Error fetching data:', error);
      // Handle error gracefully
      return null;
  }
}


fetchCarRentalData()
  .then(data => {
      if (data) {
          console.log('Fetched data:', data);
          
      } else {
          console.log('No data fetched');
      }
  })
  .catch(error => console.error('Error in fetch operation:', error));


function App() {
  return (
    <div>
      <Navbar />
      <AppRouting />
      <Footer />
    </div>
  );
}

export default App;