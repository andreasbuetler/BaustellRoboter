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
      shouldPlay: !helmetState.shouldPlay,
    });
  };
  return (
    <HelmetWrapper>
      <Title>{helmetId}</Title>
      <p>Audio: {helmetState.audio}</p>
      <PlayToggle onClick={() => togglePlay()}>
        {helmetState.shouldPlay ? "Stop" : "Play"}
      </PlayToggle>
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
  background-color: var(--main-color);
`;
export default Helmet;
