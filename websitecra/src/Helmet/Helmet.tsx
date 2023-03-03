import { DatabaseReference, update } from "firebase/database";
import styled from "styled-components";
interface HelmetProps {
  helmetId: string;
  helmetRef: DatabaseReference;
  helmetState: HelmetState;
}
const Helmet = ({ helmetId, helmetState, helmetRef }: HelmetProps) => {
  const togglePlay = () => {
    update(helmetRef, {
      audioOverride: { shouldPlay: !helmetState.audioOverride.shouldPlay },
    });
  };
  const changeAudio = (audioFileIndex: number) => {
    update(helmetRef, {
      audioOverride: {
        audioFileIndex: audioFileIndex,
      },
    });
  };
  const currentAction = helmetState?.actions?.[helmetState?.actionIndex];
  return (
    <HelmetWrapper onClick={() => togglePlay()} isPlaying={helmetState?.audioOverride?.shouldPlay}>
      <Title>{helmetId}</Title>
      <CurrentAction>
        <ul>
          {currentAction?.type === "drive" && (
            <>
            <div className="direction">
            {currentAction?.direction === "backwards" && (
              <p>backwards</p>
            )}
            {currentAction?.direction === "forwards" && (
              <p>forwards</p>
            )}
            {currentAction?.direction === "stop" && (
              <p>stop</p>
            )}
            {currentAction?.direction === "turnLeft" && (
              <p>turn left</p>
            )}
            {currentAction?.direction === "turnRight" && (
              <p>turnRight</p>
            )}
            </div>
            </>
          )}
          {currentAction?.type === "sound" && (
            <>
            <li>Audio file index: {currentAction.audioFileIndex}</li>
            </>
          )}
        </ul>
      </CurrentAction>
        {helmetState?.audioOverride?.shouldPlay ? "is playing" : "Play"}
    </HelmetWrapper>
  );
};
const Title = styled.h2`
  font-size: 2rem;
`;
const HelmetWrapper = styled.div<{isPlaying?: boolean}>`
 background-color: ${({isPlaying})=> isPlaying ? "green" : "none"};
  display: flex;
  justify-content: center;
  align-items: center;
  flex-flow: column nowrap;
  padding: 20px;
  min-height: 200px;
  border-right: thin solid white;
  border-bottom: thin solid white;
`;
const CurrentAction = styled.div``;
export default Helmet;
