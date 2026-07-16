import { useEffect, useRef } from 'react'
import Globe from 'react-globe.gl'

function App() {
  const globeEl = useRef()

  useEffect(() => {
    fetch('https://unpkg.com/world-atlas/countries-110m.json')
      .then(res => res.json())
      .then(data => {
        globeEl.current.polygonsData(data.features)
      })
  }, [])

  return (
    <Globe
      ref={globeEl}
      globeImageUrl="https://unpkg.com/three-globe/example/img/earth-blue-marble.jpg"
      backgroundImageUrl="https://unpkg.com/three-globe/example/img/night-sky.png"
      polygonCapColor={() => 'rgba(200, 200, 200, 0.25)'}
      polygonSideColor={() => 'rgba(200, 200, 200, 0.05)'}
      polygonStrokeColor={() => '#fff'}
      polygonStrokeWidth={0.5}
    />
  )
}

export default App
