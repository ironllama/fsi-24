import './Screen.css';

export function Screen(props) {
    const { display } = props;

    return (
        <div id='screen' className='border'>{display}</div>
    )
}