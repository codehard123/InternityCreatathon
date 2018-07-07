using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityStandardAssets.CrossPlatformInput;
using UnityEngine.UI;

public class boatcontroller : MonoBehaviour {
	public float inputDelay = 0.1f;
	public float forwardVel = +12;
	public float rotateVel=100f;
	Quaternion targetRotation;
	public Rigidbody rBody;
	float forwardInput,turnInput;
	public Text TextMercury;
	public Text TextCalcium;
	public Text TextOil;

	Quaternion TargetRotation
	{
		get{
			return targetRotation;
		}
	}

	// Use this for initialization
	void Start () {
		Screen.lockCursor = true;
		targetRotation = transform.rotation;
		if (GetComponent<Rigidbody> ()) {
			rBody = GetComponent<Rigidbody> ();

		}
		else
			Debug.Log ("The character needs to have a RigidBody Component attached to it");
	}
	void GetInput(){
		forwardInput=CrossPlatformInputManager.GetAxis("Vertical");
		turnInput=CrossPlatformInputManager.GetAxis("Horizontal");
	}


	// Update is called once per frame
	void Update () {
		

	}
	void FixedUpdate()
	{
		GetInput ();
		Turn ();
		Run ();
	}
	void Run()
	{
		if (Mathf.Abs (forwardInput) > inputDelay) {

			rBody.velocity= transform.forward* forwardInput * forwardVel;


		} 
		else {
			rBody.velocity = Vector3.zero;
		}
	}
	void Turn()

	{
		if (Mathf.Abs (forwardInput) > inputDelay) 
		{
			targetRotation*=Quaternion.AngleAxis(rotateVel*turnInput*Time.deltaTime,Vector3.up);

		}
		transform.rotation=targetRotation;
	}

}
