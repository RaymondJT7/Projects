import { Link } from "react-router-dom"
function Navbar() {
    const WebsiteName = "RayLabs"
  return (
    // Parent container
    <div className="animated-gradient text-emerald-400 shadow-md border-[3px] border-solid border-amber-400">
      <div className="max-w-6xl mx-auto px-6 py-4">
        <div className="flex flex-wrap justify-between items-center gap-4 md:gap-8 text-lg font-semibold">
          
          {/* Logo */}
          <div className="text-2xl font-bold text-emerald-400 animate-spin slow-spin">
            {WebsiteName}
          </div>

          {/* Menu Items */}
          <ul className="flex flex-col sm:flex-row items-center sm:items-start gap-2 sm:gap-8 font-medium text-center sm:text-left">
            <li className="hover:text-yellow-400 transition duration-200 cursor-pointer"><Link to="/">Home</Link></li>
            <li className="hover:text-yellow-400 transition duration-200 cursor-pointer"><Link to="/content">Content</Link></li>
            <li className="hover:text-yellow-400 transition duration-200 cursor-pointer"><Link to="/about">About</Link></li>
            <li className="hover:text-yellow-400 transition duration-200 cursor-pointer"><Link to="/contact">Contact</Link></li>
          </ul>
        </div>
      </div>
    </div>
  )
}

export default Navbar
