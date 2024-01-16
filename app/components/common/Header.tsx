import Link from 'next/link'

const Header = () => {

    return (
        <>
        <div className="flex items-center justify-between px-4 py-4">
            <div className="flex items-center justify-center">
                <Link href="/">
                <h1 className="font-poppins font-extrabold text-2xl text-black">
                    full-auth
                    <span className="text-[#08f]">
                        .
                    </span>
                </h1>
                </Link>
            </div>

            <div className="flex items-center justify-between">
                <Link href="/" className=' bg-inherit'>
                    <p className='text-black font-medium text-xl px-4 py-2 mr-4 transition-all duration-300 rounded-xl hover:bg-[#dcdcdc]'>
                        Login
                    </p>
                </Link>
                <Link href="/" className='bg-inherit'>
                    <p className='text-black font-medium text-xl transition-all px-4 py-2 duration-300 rounded-xl hover:bg-[#dcdcdc]'>
                        Signup
                    </p>
                </Link>
            </div>
        </div>
        <div className="bg-gradient-to-r from-[#ebebeb] via-[#d8d8d8] to-[#ebebeb] h-0.5 w-full" />
        </>

        
    );
};
  export default Header;
  