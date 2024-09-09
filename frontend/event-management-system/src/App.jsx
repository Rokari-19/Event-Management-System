import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { Menu, X } from 'lucide-react';

const LandingPage = () => {
  const [scrollY, setScrollY] = useState(0);
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setScrollY(window.pageYOffset);
    };

    window.addEventListener('scroll', handleScroll);
    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  }, []);

  return (
    <div className="relative overflow-hidden bg-gradient-to-b from-gray-100 to-gray-50">
      <nav className={`fixed top-0 left-0 w-full z-10 transition-colors duration-300 ${
        scrollY > 100 ? 'bg-gray-800 text-white' : 'bg-transparent text-gray-800'
      }`}>
        <div className="max-w-7xl mx-auto flex justify-between items-center py-4 px-4 sm:px-6 lg:px-8">
          <a href="#" className="text-lg font-bold">Event Management</a>
          <div className="hidden md:flex space-x-4">
            <a href="#" className="hover:text-gray-300">About</a>
            <a href="#" className="hover:text-gray-300">Contact</a>
          </div>
          <button
            className="md:hidden p-2 rounded-md hover:bg-gray-200 transition-colors duration-300 focus:outline-none"
            onClick={() => setIsMenuOpen(!isMenuOpen)}
          >
            {isMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
          </button>
        </div>
        {isMenuOpen && (
          <div className="md:hidden bg-gray-800 text-white py-4 px-6 space-y-2">
            <a href="#" className="block hover:text-gray-300">About</a>
            <a href="#" className="block hover:text-gray-300">Contact</a>
          </div>
        )}
      </nav>

      <div className="h-screen flex items-center justify-center relative">
        <div className="max-w-7xl mx-auto text-gray-800 text-center z-10 px-4 sm:px-6 lg:px-8">
          <motion.h1
            initial={{ y: 50, opacity: 0 }}
            animate={{ y: 0, opacity: 1 }}
            transition={{ duration: 1 }}
            className="text-4xl font-bold mb-4"
          >
            Elevate Your Events
          </motion.h1>
          <motion.p
            initial={{ y: 50, opacity: 0 }}
            animate={{ y: 0, opacity: 1 }}
            transition={{ duration: 1, delay: 0.2 }}
            className="text-lg mb-8"
          >
            Our event management app helps you plan, organize, and execute events with ease.
          </motion.p>
          <motion.button
            initial={{ y: 50, opacity: 0 }}
            animate={{ y: 0, opacity: 1 }}
            transition={{ duration: 1, delay: 0.4 }}
            className="bg-indigo-500 hover:bg-indigo-600 text-white font-bold py-3 px-6 rounded-lg"
          >
            Get Started
          </motion.button>
        </div>
        <div
          className={`absolute bottom-0 left-0 w-full h-32 bg-gradient-to-t from-gray-50 to-transparent ${
            scrollY > 100 ? 'opacity-100' : 'opacity-0'
          }`}
        />
      </div>
    </div>
  );
};

export default LandingPage;