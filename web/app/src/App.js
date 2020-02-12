import React, {Component} from 'react';
import {HexGrid, Layout, Hexagon, GridGenerator} from 'react-hexgrid';
import './App.css';
import EntityLayout from "./Layout/EntityLayout";
import HexLayout from "./Layout/HexLayout";
import PlayingCards from "./Layout/PlayingCards";

class App extends Component {
    render() {
        return (
            <div className="app">
                <div>
                <button style={{display:"flex", float:"left"}} onClick={() => window.location.reload(false)}>Change Character</button>
                </div>
                <div>
                    <p>Character Name: {this.props.characterName}</p>
                    <p>Character Card Hand: {this.props.characterCardHand}</p>
                </div>
                <h1>Drag & drop</h1>
                <HexGrid width={1300} height={500} viewBox="-50 -50 100 100">
                    <HexLayout/>
                    <EntityLayout/>
                </HexGrid>

                <PlayingCards/>
            </div>
        );
    }
}

export default App;
