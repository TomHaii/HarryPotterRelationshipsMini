import { RelationshipGraph } from ".././components/RelationshipGraph";
import { ProSidebar, Menu, MenuItem, SubMenu } from "react-pro-sidebar";
import "react-pro-sidebar/dist/css/styles.css";
import results from ".././results.json";
import { useState } from "react";
import { About } from "./About";
import { capitalizeFirstLetterOfName } from "../utils/StringUtils";
export const Main = () => {
  const [activeCharacter, setActiveCharacter] = useState(null);
  const [activeCharacterRelationship, setActiveCharacterRelationship] =
    useState({});
  const setViewpointChar = (char, index) => {
    setActiveCharacter(capitalizeFirstLetterOfName(Object.keys(char)[0]));
    setActiveCharacterRelationship(results[index][Object.keys(char)]);
  };

  const goToAboutPage = () => {
    setActiveCharacter(null);
    setActiveCharacterRelationship({});
  };
  return (
    <div>
      <div style={{ float: "left" }}>
        <ProSidebar>
          <Menu iconShape="square">
            {/* <MenuItem
              onClick={() => {
                goToAboutPage();
              }}
            >
              About
            </MenuItem> */}
            <SubMenu title="Characters" open={true}>
              {results.map((char, index) => (
                <MenuItem
                  onClick={() => {
                    setViewpointChar(char, index);
                  }}
                >
                  {capitalizeFirstLetterOfName(Object.keys(char)[0])}
                </MenuItem>
              ))}
            </SubMenu>
          </Menu>
        </ProSidebar>
      </div>
      {activeCharacter ? (
        <RelationshipGraph
          character={activeCharacter}
          characterRelationships={Object.entries(activeCharacterRelationship)}
        ></RelationshipGraph>
      ) : (
        <About></About>
      )}
    </div>
  );
};
