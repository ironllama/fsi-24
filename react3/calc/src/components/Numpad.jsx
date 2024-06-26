import "./Numpad.css";

const numkeys = [
  ["7", "8", "9"],
  ["4", "5", "6"],
  ["1", "2", "3"],
  ["C", "0", ""],
];

export function Numpad({ keyPressed }) {
  return (
    <div id="numPad">
      {numkeys.map((keyRow, i) => (
        <div key={`numRow-${i}`} className="numRow">
          {keyRow.map((key, k) => (
            <button key={`num-${k}`} className="key border" onClick={() => keyPressed(key)}>
              {key}
            </button>
          ))}
        </div>
      ))}
    </div>
  );
}
