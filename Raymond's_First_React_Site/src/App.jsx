import Navbar from './components/mainNavbar.jsx'
import Home from "./pages/Home"
import Content from './pages/Content.jsx'
import About from "./pages/About"
import Contact from "./pages/Contact"
import Footer from './components/footer.jsx'
import {Routes, Route} from "react-router-dom"

function App() {

  return (
    <>

        {/* Navbar component */}
        <Navbar />
        <Routes>
            <Route path="/" element={<Home/>} />
            <Route path="/content" element={<Content/>} />
            <Route path="/about" element={<About/>} />
            <Route path="/contact" element={<Contact/>} />
        </Routes>
        {/* Footer component */}
            <Footer /> 

    </>
  )
} 

export default App
