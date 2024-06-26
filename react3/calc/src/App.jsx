import { useState } from "react";
import "./App.css";
import { Screen } from "./components/Screen";
import { Numpad } from "./components/Numpad";
import { Operpad } from "./components/Operpad";

const operations = ["+", "-"];

function App() {
  const [buffer, setBuffer] = useState("");
  const [showingTotal, setShowingTotal] = useState(false);

  const addToBuffer = (newChar) => {
    if (newChar === "=") {
      if (showingTotal) return;

      let left = 0;
      let right = 0;
      let operChar = "";

      for (const oper of operations) {
        const operPos = buffer.indexOf(oper);
        if (operPos !== -1) {
          operChar = oper;
          [left, right] = buffer.split(oper).map((x) => parseInt(x));
          break;
        }
      }

      let total = 0;
      if (operChar === "+") total = left + right;
      else if (operChar === "-") total = left - right;

      setBuffer("" + total);
      setShowingTotal(true);
    }
    else if (newChar === "C") setBuffer("");
    else if ("+-".includes(newChar)) {
      if (
        buffer === "" ||
        buffer.includes("+") ||
        buffer.includes("-")
      ) return;

      setBuffer(buffer + newChar);
      setShowingTotal(false);
    }
    else {
      if (showingTotal) {
        setBuffer(newChar);
        setShowingTotal(false);
      }
      else setBuffer(buffer + newChar);
    }
  };

  return (
    <div id="calc" className="border">
      <Screen display={buffer} />
      <div className="allKeys">
        <Numpad keyPressed={addToBuffer} />
        <Operpad keyPressed={addToBuffer} />
      </div>
    </div>
  );
}

export default App;
