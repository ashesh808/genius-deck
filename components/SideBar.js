import React from 'react'

const SideBar = ({children}) => {
  return (
    <div className="flex h-full">
        <div className="md:flex flex-col gap y-2 bg-black h-full w-[300px] p-2">
            {children}
        </div>
    </div>
  )
}

export default SideBar;

