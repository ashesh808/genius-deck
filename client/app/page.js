import './globals.css';
import '@fontsource/roboto/300.css';
import SideBar from '@/components/SideBar';
import { Button, ButtonGroup } from '@mui/material';
export default function Home() {
	return (
		<div className='flex h-full'>
			<div className='items-left justify-left md:w-[20%] sm:w-[30%]'>
				<SideBar />
			</div>
			<div className='flex flex-col w-full items-center mt-[27vh]'>
				<div className='flex text-5xl text-center'>
					Welcome to Genius Deck
				</div>
				<div className='flex mt-5 text-3xl text-center w-[50%]'>
					Revolutionizing student learning with AI generated flashcards
				</div>
				<div className='mt-5'>
					<ButtonGroup className='gap-x-4'>
						<Button
							variant='contained'
							href='/SignUp'
							className='text-2xl'>
							Sign Up
						</Button>
						<Button
							className='text-2xl'
							variant='contained'
							href='/SignIn'>
							Sign In
						</Button>
					</ButtonGroup>
				</div>
			</div>
		</div>
	);
}
