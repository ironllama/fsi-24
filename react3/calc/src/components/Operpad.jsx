import "./Operpad.css";

const keys = ["+", "-", "="];

export function Operpad({ keyPressed }) {
    return (
        <div id="operpad">
            {keys.map((key, i) => (
                <button key={`oper-${i}`} className="key border" onClick={() => keyPressed(key)}>
                    {key}
                </button>
            ))}
        </div>
    );
}
