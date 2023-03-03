import { DatabaseReference, update } from "firebase/database";
import styled from "styled-components";
import backwards from "../icon/backwards.png";
import forwards from "../icon/forwards.png";
import left from "../icon/left.png";
import stop from "../icon/stop.png";
import right from "../icon/right.png";
import soundRed from "../icon/sound_red.png";
import sound from "../icon/sound.png";
interface HelmetProps {
  helmetId: string;
  helmetRef: DatabaseReference;
  helmetState: HelmetState;
}
const Helmet = ({ helmetId, helmetState, helmetRef }: HelmetProps) => {
  const currentAction = helmetState?.actions?.[helmetState?.actionIndex];
  const togglePlay = () => {
    update(helmetRef, {
      audioOverride: {
        audioFileIndex: helmetState.audioOverride.audioFileIndex,
        shouldPlay: !helmetState.audioOverride.shouldPlay,
      },
    });
  };
  const changeAudio = (audioFileIndex: number) => {
    update(helmetRef, {
      audioOverride: {
        audioFileIndex: audioFileIndex,
        shouldPlay: true,
      },
    });
  };
  return (
    <HelmetWrapper onClick={() => togglePlay()} isPlaying={helmetState?.audioOverride?.shouldPlay}>
      <Title>{helmetId}</Title>
      <CurrentAction>
        <ul>
        {!helmetState?.audioOverride?.shouldPlay && <>

            {currentAction?.type === "drive" && (
              <>
                <div className="direction">

                  {currentAction?.direction === "backwards" && (
                    <>
                      <img className="direction__icon" src={backwards} alt="backwards arrow" />
                    </>

                  )}
                  {currentAction?.direction === "forwards" && (
                    <>
                      <img className="direction__icon" src={forwards} alt="forward arrow" />
                    </>

                  )}
                  {currentAction?.direction === "stop" && (
                    <>
                      <img className="direction__icon" src={stop} alt="Stop sign" />
                    </>
                  )}
                  {currentAction?.direction === "turnLeft" && (
                    <>
                      <img className="direction__icon" src={left} alt="left arrow" />
                    </>
                  )}
                  {currentAction?.direction === "turnRight" && (
                    <>
                      <img className="direction__icon" src={right} alt="right arrow" />
                    </>
                  )}
                </div>
              </>
            )}
            {currentAction?.type === "sound" && (
              <>
                <img className="direction__icon" src={sound} alt="sound icon" />
              </>
            )}
          </>

          }
          {helmetState?.audioOverride?.shouldPlay &&
            <img className="direction__icon--sound" src={soundRed} alt="sound icon" />
          }
        </ul>
      </CurrentAction>
    </HelmetWrapper>
  );
};
const Title = styled.h2`
  font-size: 2rem;
`;
const HelmetWrapper = styled.div<{ isPlaying?: boolean }>`
  background-color: ${({ isPlaying }) => isPlaying ? "white" : "none"};
  color: ${({ isPlaying }) => isPlaying ? "var(--main-red)" : "none"};
  display: flex;
  justify-content: center;
  align-items: center;
  flex-flow: column nowrap;
  padding: 20px;
  min-height: 200px;
  border-right: thin solid white;
  border-bottom: thin solid white;
  &:nth-child(even) {
      border-right: none;
    }
`;
const CurrentAction = styled.div`
width: 100px;
`;
export default Helmet;