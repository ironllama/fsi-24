import "./ProfileTile.css";

export function ProfileTile({ person }) {
    const renderStars = (num) => {
        const allStars = [];

        for (let i = 0; i < num; i++) {
            allStars.push(
                <img
                    key={`profileImg-${i}`}
                    className="ratingStar"
                    src="https://imgs.search.brave.com/1YY_6wwbaaVZfSRkVqFepZwB7iX-VxCNAwcIkSqlmS8/rs:fit:860:0:0/g:ce/aHR0cHM6Ly91cGxv/YWQud2lraW1lZGlh/Lm9yZy93aWtpcGVk/aWEvY29tbW9ucy9l/L2U3L0ZlYXR1cmVk/X2FydGljbGVzX3N0/YXJfbW9kZXJuLnN2/Zw.svg"
                />
            );
        }

        return allStars;
    };

    return (
        <li className="profileTile">
            <div className="picWrapper">
                <img src={person.pic} />
            </div>
            <div className="textStuff">
                <div className="name">
                    {person.name} - {person.age}
                </div>
                <div className="occupation">{person.occupation}</div>
                <div className="rating">
                    {renderStars(person.rating)}
                    <span className="ratingNum">({person.rating}/10)</span>
                </div>
            </div>
        </li>
    );
}
