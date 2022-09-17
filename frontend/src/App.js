import logo from './logo.svg';
import './App.css';
import SideBar from './components/SideBar';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Reports from './pages/Reports';
import UploadFile from './pages/UploadFile';

function App() {
  return (
    <div className="App">
        <Router>
        <SideBar />
        <Routes>
          <Route path='/' element={<Home/>} />
          <Route path='/reports' element={<Reports />} />
          <Route path='/upload' element={<UploadFile />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
