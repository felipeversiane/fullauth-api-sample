import Link from "next/link";


const HeroHome = () => (
    <div className="flex items-center px-4 mt-20 flex-col justify-center h-[20rem]">
        <div className=" w-full flex justify-start items-start">
            <h1 className="font-bold text-6xl text-black">
            Full auth RESTful API
            </h1>
        </div>

        <div className=" flex items-start justify-start w-full mt-6">
            <div className=" w-10/12">
            <p className="font-regular text-xl">
            This project was made with the aim of testing my skills and learning more about authentication in django, using the djoser library I was able to apply a complete authentication system, test it with me!
            </p>
            </div>
        </div>

    </div>
  )
  export default HeroHome;
  