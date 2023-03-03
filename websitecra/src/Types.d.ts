type DriveAction = {
  type: "drive";
  direction: "forwards" | "backwards" | "turnLeft" | "turnRight" | "stop";
  length: number;
};
type SoundAction = {
  type: "sound";
  audioFileIndex: number;
  shouldPlay: boolean;
};
type HelmetAction = DriveAction | SoundAction;

type HelmetState = {
  actionIndex: number;
  actions: HelmetAction[];
  audioOverride: {
    audioFileIndex: number;
    shouldPlay: boolean;
  };
};
interface HelmetStates {
  [x: string]: HelmetState;
}
