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
    <HelmetWrapper>
      <Title>{helmetId}</Title>
      <CurrentAction>
        <ul>
          <li>Current action Index: {helmetState?.actionIndex}</li>
          {currentAction?.type === "drive" && (
            <>
            <li><b>Driving</b></li>
            <li>Direction: {currentAction.direction}</li>
            <li>Length: {currentAction.length}</li>
            </>
          )}
          {currentAction?.type === "sound" && (
            <>
            <li><b>Playing sound</b></li>
            <li>Audio file index: {currentAction.audioFileIndex}</li>
            </>
          )}
        </ul>
      </CurrentAction>
      <p>Play an audio:</p>
      <PlayToggle onClick={() => togglePlay()}>
        {helmetState?.audioOverride?.shouldPlay ? "Stop" : "Play"}
      </PlayToggle>
      {Array.from(Array(4).keys()).map((i) => (
        <AudioFileButton onClick={() => changeAudio(i)} key={i}>
          {i}
        </AudioFileButton>
      ))}
    </HelmetWrapper>
  );
};
const Title = styled.h2`
  font-size: 2rem;
`;
const HelmetWrapper = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  flex-flow: column wrap;
  max-width: 900px;
  margin: 0 auto;
  padding: 20px;
  margin-bottom: var(--main-margin);
`;
const PlayToggle = styled.button`
  all: unset;
  background-color: var(--main-color);
`;
const AudioFileButton = styled.button`
  all: unset;
  background-color: var(--main-color);
`;
const CurrentAction = styled.div``;
export default Helmet;
