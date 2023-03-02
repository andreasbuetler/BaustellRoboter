import React, { useEffect } from "react";
import styled from "styled-components";
import { FirebaseApp, initializeApp } from "firebase/app";
import { Database, DatabaseReference, getDatabase, onValue, ref } from "firebase/database";
import Helmet from "./Helmet";

function App() {
  const [firebaseApp, setFirebaseApp] = React.useState<FirebaseApp>();
  const [database, setDatabase] = React.useState<Database>();
  const [helmetStatesRef, setHelmetStatesRef] = React.useState<DatabaseReference>();
  const [allHelmetStates, setAllHelmetStates] = React.useState<HelmetStates>();
  useEffect(() => {
    // TODO: Replace the following with your app's Firebase project configuration
    const firebaseConfig = {
      apiKey: "AIzaSyDXBwmM2wX7GjkNgNC7TiCp1p2wX4OO-CE",
      authDomain: "baustellrobots.firebaseapp.com",
      databaseURL:
        "https://baustellrobots-default-rtdb.europe-west1.firebasedatabase.app",
      projectId: "baustellrobots",
      storageBucket: "baustellrobots.appspot.com",
      messagingSenderId: "11767442225",
      appId: "1:11767442225:web:085899e2179717ef511e10",
    };
    const app = initializeApp(firebaseConfig);
    const databaseNew = getDatabase(app);
    setDatabase(databaseNew);
    setFirebaseApp(app);
    const helmetStatesRefNew = ref(databaseNew, "helmetStates/");
    setHelmetStatesRef(helmetStatesRefNew);
    onValue(helmetStatesRefNew, (snapshot) => {
      const allHelmetsNew = snapshot.val();
      setAllHelmetStates(allHelmetsNew);
    });
  }, []);

  return (
    <AppWrapper>
      <Logo>
        <img src="https://baustell.ch/images/baulogo.png" alt="baustell logo" />
      </Logo>
      <Intro>
        <p>
          Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend
          tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac,
          enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus.
          Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum.
          Aenean imperdiet. Etiam ultricies nisi vel augue.
        </p>
      </Intro>
      {allHelmetStates && helmetStatesRef && database && (
        <InteractiveStuff>
          {Object.keys(allHelmetStates).map((helmetId) => {
            const helmetState = allHelmetStates[helmetId];
            const helmetRef = ref(database, `helmetStates/${helmetId}`);
            return (
              <Helmet key={helmetId} helmetId={helmetId} helmetRef={helmetRef} helmetState={helmetState} />
            );
          })}
        </InteractiveStuff>
      )}
    </AppWrapper>
  );
}
const AppWrapper = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  flex-flow: column wrap;
  max-width: 900px;
  margin: 0 auto;
`;
const Logo = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: var(--main-margin);
  img {
    width: 250px;
  }
`;
const Intro = styled.div`
  color: white;
  font-size: 24px;
  text-align: center;
  margin-bottom: var(--main-margin);
`;
const InteractiveStuff = styled.div``;
export default App;
