import './Numpad.css';

const numkeys = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['', '0', '']
]

export function Numpad() {
    return (
        <div id='numPad'>
            {numkeys.map(keyRow => (
                <div className="numRow">
                    {keyRow.map(key => (
                        <div className="numKey border">{key}</div>
                    ))}
                </div>
            ))}
        </div>
    )
}