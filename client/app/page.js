import './globals.css';
import '@fontsource/roboto/400.css';
import SideBar from '@/components/SideBar';
import { Button, ButtonGroup, Divider } from '@mui/material';
import PersonAddIcon from '@mui/icons-material/PersonAdd';
import PersonIcon from '@mui/icons-material/Person';
export default function Home() {
	return (
		<div className='flex h-full'>
			<div className='h-[100%] items-left justify-left md:w-[20%] sm:w-[30%]'>
				<SideBar />
			</div>
			<div className='flex flex-col w-full items-center mt-[15vh]'>
				<div className='flex text-6xl text-center'>
					Welcome to Genius Deck
				</div>
				<div className='flex mt-5 text-3xl text-center w-[50%] items-center justify-center'>
					Revolutionizing student learning with AI generated
					flashcards
				</div>
				<div className='mt-7'>
					<ButtonGroup className='gap-x-4'>
						<Button
							startIcon={<PersonAddIcon />}
							variant='contained'
							href='/Signup'
							className='text-2xl'>
							Sign Up
						</Button>
						<Button
							startIcon={<PersonIcon />}
							className='text-2xl'
							variant='contained'
							href='/Login'>
							Sign In
						</Button>
					</ButtonGroup>
				</div>
				<Divider className='mt-[5vh] w-[80%]' />
				<div className='text-5xl mt-[5vh]'>Here is how it works!</div>
				<div className='mt-9'>
					<iframe
						width='800'
						height='504'
						src={
							'https://www.youtube.com/embed/VhDkrxmsLAY?si=V3I6KIachvWubPjr&mute=1&vq=hd72'
						}
						allowFullScreen
					/>
				</div>
			</div>
		</div>
	);
}
