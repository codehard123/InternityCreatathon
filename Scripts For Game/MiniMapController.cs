using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class MapObject {
	public Image icon { get; set;}
	public GameObject owner{ get; set;}
	public int flag=0;

}
public class MiniMapController:MonoBehaviour{
	public Transform playerPos;
	public Camera mapCamera;
	public static List<MapObject> mapObjects=new List<MapObject>();
	public static void RegisterMapObject(GameObject o,Image i)
	{
		Image image = Instantiate (i);
		mapObjects.Add (new MapObject (){ owner = o, icon = image });
	}
	public static void RemoveMapObject(GameObject o)
	{   List<MapObject> newList = new List<MapObject> ();
		for (int i = 0; i < mapObjects.Count; i++) {
			if (mapObjects [i].owner == o) {
				Destroy (mapObjects [i].icon);
				continue;
			} else
				newList.Add (mapObjects [i]);
		}
		mapObjects.RemoveRange (0, mapObjects.Count);
		mapObjects.AddRange (newList);
	}
	void DrawMapIcons()
	{
		foreach (MapObject mo in mapObjects) {
 			Vector2 mop = new Vector2 (mo.owner.transform.position.x, mo.owner.transform.position.y);
			Vector2 pp = new Vector2 (playerPos.position.x, playerPos.position.y);
			if (Vector2.Distance (mop, pp) > 70) {
				mo.icon.enabled = false;
				continue;
			
			} else {
				if(mo.flag==0)
				mo.icon.enabled = true;
			}
			if (Vector2.Distance (mop, pp) < 1) {
				mo.icon.enabled = false;
				mo.flag = 1;
			}

			Vector3 screenPos = mapCamera.WorldToViewportPoint(mo.owner.transform.position);
			mo.icon.transform.SetParent (this.transform);
			RectTransform rt = this.GetComponent<RectTransform> ();
			Vector3[] corners = new Vector3[4];
			rt.GetWorldCorners (corners);
			screenPos.x = Mathf.Clamp(screenPos.x * rt.rect.width+corners[0].x,corners[0].x,corners[2].x);

			screenPos.y = Mathf.Clamp(screenPos.y * rt.rect.height+corners[0].y,corners[0].y,corners[1].y);
			screenPos.z = 0;
			mo.icon.transform.position = screenPos;
		}
	}
	void Update()
	{
		DrawMapIcons ();
	}


}

	
