
function Footer() {
  // Variables  

  return (
    <>
        <div className="bg-[url('./assets/Footer-Bg.png')] bg-cover bg-no-repeat bg-center py-10 text-center text-white">

            {/* Footer Logo and Headings Section */}
            <div className="flex flex-row items-start md:items-center justify-center gap-75 text-2xl sm:text-3xl md:text-3xl lg:text-3xl text-emerald-400 px-6 mb-5">
                <img src="src/assets/Logo.png" alt="Logo image" className="w-20" />
                <h1 className="font-bold">Nav Links:</h1>
                <h1 className="font-bold">Contact Details:</h1>
            </div>    

            {/* Footer Content Section */}
            {/* <div className="flex flex-row items-start md:items-center justify-start gap-4 md:gap-32">

                <p className="">This is a paragraph</p> */}

                {/* Menu Items */}
                {/* <ul className="gap-4 md:gap-8 font-medium">
                    <li className="hover:text-yellow-400 transition duration-200 cursor-pointer">Home</li>
                    <li className="hover:text-yellow-400 transition duration-200 cursor-pointer">Content</li>
                    <li className="hover:text-yellow-400 transition duration-200 cursor-pointer">About</li>
                    <li className="hover:text-yellow-400 transition duration-200 cursor-pointer">Contact</li>
                </ul> */}

                {/* <ul className="gap-4 md:gap-8 font-medium">
                    <li>Contact Number: 0634547847</li>
                    <li>Email Address: rjtilstone7@gmail.com</li>
                </ul>
            </div> */}
        </div>

    </>
  )
} 

export default Footer

