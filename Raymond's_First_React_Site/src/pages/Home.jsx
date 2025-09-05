import Footer from "../components/footer"
function Home(){
    // Variables
    const WebsiteName = "RayLabs"


    return(
        <>
            {/* Parent container to hold the hero section as a whole */}
            <div className="min-h-screen flex items-center justify-center bg-[url('./assets/Home-Bg.jpg')] bg-cover bg-no-repeat bg-center text-white px-6">
                
                {/* Hero section */}
                <div className="max-w-3xl text-center">
                    <h1 className="text-5xl font-extrabold mb-4 leading-tight">
                        Welcome to <span className="text-yellow-300">{WebsiteName}</span>
                    </h1>
                    <p className="text-lg text-gray-200 mb-6">
                        This is my first React test application — a space to experiment, learn, and build functional interfaces with Tailwind CSS and modern components.
                        This is the environment where all of my tailwindcss and react projects and components will show.
                    </p>
                    <button className="bg-yellow-300 text-black font-semibold px-6 py-2 rounded hover:bg-yellow-400 transition duration-200 animate-bounce">
                            Get Started
                    </button>

                    <h2 className="text-3xl font-bold mt-16 mb-4 text-yellow-300 animate-pulse">
                        Why {WebsiteName} Exists
                    </h2>
                    <p className="text-lg text-gray-200 animate-pulse">
                        {WebsiteName} is more than just a testbed — it's a creative playground where ideas take shape through code. Whether you're experimenting with layout techniques, refining component logic, or exploring new design patterns, this space is built to grow with you. Every section, every interaction, is a reflection of your journey as a developer.
                    </p>

                </div>
            </div>
        </>
    )    
}

export default Home