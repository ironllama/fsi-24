import { useRef, useState } from "react";
import { ProfileTile } from "./components/ProfileTile";
import "./App.css";

const startPeople = [
    {
        name: "Peter",
        pic: "https://images.generated.photos/Myb_oEYaK_lKdaxBRexhpW0HvXv-rKeQl86R7pnkIq4/rs:fit:256:256/czM6Ly9pY29uczgu/Z3Bob3Rvcy1wcm9k/LnBob3Rvcy92M18w/OTUyMzQwLmpwZw.jpg",
        occupation: "Musician",
        age: 34,
        rating: 8,
    },
    {
        name: "Paul",
        pic: "https://images.generated.photos/aS0arhlLqb14uMy9kutZSURtErE8dGlKZT3js-Yi2wc/rs:fit:256:256/czM6Ly9pY29uczgu/Z3Bob3Rvcy1wcm9k/LnBob3Rvcy92M18w/MzkzNjU4LmpwZw.jpg",
        occupation: "Carpenter",
        age: 27,
        rating: 7,
    },
    {
        name: "Mary",
        pic: "https://images.generated.photos/KLrw4DrMRHMB69wxMmkyrJLHWDNSQ_LlerM3woEux7s/rs:fit:256:256/czM6Ly9pY29uczgu/Z3Bob3Rvcy1wcm9k/LnBob3Rvcy92M18w/NDExMjM2LmpwZw.jpg",
        occupation: "Physicist",
        age: 29,
        rating: 9,
    },
    {
        name: "Karen",
        pic: "https://images.generated.photos/Aq6GPaB88jRoU1GGcMnozHO521KuJpGQabSJCf7wbtU/rs:fit:256:256/czM6Ly9pY29uczgu/Z3Bob3Rvcy1wcm9k/LnBob3Rvcy92M18w/MDE3ODgwLmpwZw.jpg",
        occupation: "Soccer Mom",
        age: 50,
        rating: 1,
    },
];

export default function App() {
    const [people, setPeople] = useState(startPeople);
    // const [origPeople, setOrigPeople] = useState(startPeople);  // Can use instead of useRef.

    const origPeople = useRef(startPeople);

    const handleSearch = (evt) => {
        // console.log(evt);
        if (evt.target.value.length >= 3) {
            // let newPeople = [...startPeople];  // Can use global, but better to keep in component.
            let newPeople = [...origPeople.current];
            newPeople = newPeople.filter((p) =>
                p.name.toLowerCase().includes(evt.target.value.toLowerCase())
            );
            setPeople(newPeople);
        } else {
            // setPeople(startPeople);  // Can use global, but better to keep in component.
            setPeople(origPeople.current);
        }
    };

    return (
        <div className="App">
            <div className="searchWrapper">
                <input
                    onChange={handleSearch}
                    placeholder="Search for..."
                    type="search"
                />
            </div>
            <ul>
                {people.map((p) => (
                    <ProfileTile key={`person-${p.name}`} person={p} />
                ))}
            </ul>
        </div>
    );
}
