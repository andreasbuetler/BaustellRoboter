import React, { useEffect } from "react";
import styled from "styled-components";
import { FirebaseApp, initializeApp } from "firebase/app";
import {
  Database,
  DatabaseReference,
  getDatabase,
  onValue,
  ref,
} from "firebase/database";
import Helmet from "./Helmet";

function App() {
  const [firebaseApp, setFirebaseApp] = React.useState<FirebaseApp>();
  const [database, setDatabase] = React.useState<Database>();
  const [helmetStatesRef, setHelmetStatesRef] =
    React.useState<DatabaseReference>();
  const [allHelmetStates, setAllHelmetStates] = React.useState<HelmetStates>();
  const [helmetIdInUrl, setHelmetIdInUrl] = React.useState<
    string | undefined
  >();
  useEffect(() => {
    const searchParams = new URL(String(window.location)).searchParams;
    const helmetId = searchParams.get("helmet");
    helmetId && setHelmetIdInUrl(helmetId);
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
      {allHelmetStates && helmetStatesRef && database && (
        <InteractiveStuff>
          {Object.keys(allHelmetStates).map((helmetId) => {
            const helmetState = allHelmetStates[helmetId];
            const helmetRef = ref(database, `helmetStates/${helmetId}`);
            const isInUrl = helmetIdInUrl === helmetId
            return (
              <Helmet
                key={helmetId}
                helmetId={helmetId}
                helmetRef={helmetRef}
                helmetState={helmetState}
                isInUrl={isInUrl}
              />
            );
          })}
          <div className="logo__intro">
            <Logo>
              <img
                src="https://baustell.ch/images/baulogo.png"
                alt="baustell logo"
              />
            </Logo>
            <Intro>
              <p>Baustell Robots Sound Controller.</p>
            </Intro>
          </div>
        </InteractiveStuff>
      )}
    </AppWrapper>
  );
}
const AppWrapper = styled.div``;
const InteractiveStuff = styled.div`
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 1fr 1fr;
`;
const Logo = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: var(--main-margin);
  img {
    width: 100px;
  }
`;
const Intro = styled.div`
  color: white;
  font-size: 18px;
  text-align: center;
`;
export default App;
