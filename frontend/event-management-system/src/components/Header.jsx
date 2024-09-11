// import { Link } from "lucide-react";
import { useState } from "react";
import { Link } from "react-router-dom";

export default function Header() {

  let [isOpen, setisOpen] = useState(false);

  return (
    <div className="shadow-md w-full border-bottom border-gray-700 fixed top-0 left-0">
      <div className="md:px-10 py-4 px-7 md:flex justify-between bg-white">
        {/* image here */}
        <div className="flex text-2-xl cursor-pointer items-center gap-2">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            strokeWidth={1.5}
            stroke="currentColor"
            className="size-6 w-7 h-7 text-green-600"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              d="M6.75 3v2.25M17.25 3v2.25M3 18.75V7.5a2.25 2.25 0 0 1 2.25-2.25h13.5A2.25 2.25 0 0 1 21 7.5v11.25m-18 0A2.25 2.25 0 0 0 5.25 21h13.5A2.25 2.25 0 0 0 21 18.75m-18 0v-7.5A2.25 2.25 0 0 1 5.25 9h13.5A2.25 2.25 0 0 1 21 11.25v7.5"
            />
          </svg>
          <span className="font-bold">AfroFEST.com</span>
        </div>

        <div
          onClick={() => setisOpen(!isOpen)}
          className="w-7 h-7 absolute right-8 top-6 cursor-pointer md:hidden"
        >
          {isOpen ? (
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              strokeWidth={1.5}
              stroke="currentColor"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                d="M6 18 18 6M6 6l12 12"
              />
            </svg>
          ) : (
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              strokeWidth={1.5}
              stroke="currentColor"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                d="M3.75 5.25h16.5m-16.5 4.5h16.5m-16.5 4.5h16.5m-16.5 4.5h16.5"
              />
            </svg>
          )}
        </div>

        {/* nav links here, meshack. routing work later */}

        <ul
          className={`md:flex pl-9 md:pl-0 md:ml-8 md:items-center md:pb-0 pb-12 md:static absolute md:z-auto z-[-1] left-0 w-full transition-all bg-white duration-500 ease-out
            ${isOpen ? "top-12" : "top-[-490px]"}`}
        >
          <li className="font-semibold my-7 md:my-0 md:ml-8">
            <Link to="/about"> Home</Link>
          </li>

          <li className="font-semibold my-7 md:my-0 md:ml-8">
            <Link to="/about"> Help & Support</Link>
          </li>
          <li className="font-semibold my-7 md:my-0 md:ml-8">
            <Link to="/about"> About AfroFEST</Link>
          </li>

          <button className="btn bg-green-400 rounded-lg py-1 px-3 md:ml-8 md:static">
            Create An Event
          </button>
        </ul>
      </div>
    </div>
  );
}
