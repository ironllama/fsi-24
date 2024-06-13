// function MyButton(props) {
// const { counter, onSpecial } = props;  // Destructure

// Eliminate the intermediate variable and destructure in the function parameter list.
function MyButton({ counter, onSpecial }) {

    // function handleClick() {
    //     console.log("CLICKED!");
    // }

    return (
        // Using local function to handle the click.
        // <button onClick={handleClick}>

        // Using the incoming properties
        // <button onClick={props.onSpecial}>
        //     Count is {props.counter}
        // </button>

        // Using the incoming properties post-destructuring
        <button onClick={onSpecial}>
            Count is {counter}
        </button>
    );
}

// export default function MyApp() {
function MyApp() {
    // let counter = 0;  // Standard local variable.
    const [counter, setCounter] = React.useState(0);  // State variable

    let jCounter = 0;

    const names = ["Pedro", "Marco", "Anna", "Juanita"];
    function renderAllWelcomes() {
        const allWelcomes = [];

        function adjustCounter(name = "") {
            if (name === "Juanita") {
                jCounter += 1;
                console.log("JCOUNTER:", jCounter);
            }
            else {
                setCounter(counter + 1);
                console.log("NEW COUNTER:", counter + 1);
            }
        }

        // for (let i = 0; i < 10; i++) {
        for (let i = 0; i < names.length; i++) {
            // for (const name of names) {
            allWelcomes.push(
                <div key={`welcomes-${i}`}>
                    <h1
                        style={{
                            color: "goldenrod",
                            fontSize: "1rem"
                        }}
                    >Welcome to my app, {names[i]}</h1>

                    {/* Using the MyButton component. */}
                    <MyButton counter={counter} onSpecial={() => adjustCounter(names[i])} />

                    {/* Using own version of button (not using MyButton component) */}
                    {/* <button onClick={() => {
                        // counter += 1;  // Only works to change local variable

                        // setCounter(counter + 1)  // Change useState variable
                        // setCounter(c => {  // Change useState with function
                        //     const new_c = c + 1
                        //     console.log("NEW COUNTER:", new_c);
                        //     return new_c;
                        // });

                        adjustCounter(names[i]);  // Move logic into another function

                        // You can still change the DOM directly, but this is frowned upon w/ React.
                        // document.querySelector("#numCounter").innerHTML = counter;
                    }}>
                        I'm a button
                    </button> */}
                </div>
            )
        }
        return allWelcomes;
    }


    return (
        <div>
            <div id="numCounter">{counter}</div>
            {renderAllWelcomes()}
        </div>
    );
}
